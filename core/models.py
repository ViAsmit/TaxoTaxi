from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    mobile = models.CharField(max_length=10)
    mobile_verified = models.BooleanField(default=False)
    profile_pic = models.ImageField(blank = True, null = True)
    wallet_balance = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.username

class banner(models.Model):
    image = models.ImageField()
    h2 = models.CharField(max_length=256)
    h5 = models.CharField(max_length=256)

    def __str__(self):
        return self.h2

    class Meta:
        verbose_name_plural = 'Main Page Banners'

class popular_destinations(models.Model):
    from_place = models.CharField(max_length=104)
    to_place = models.CharField(max_length=104)
    popular_place = models.CharField(max_length=104)
    distance = models.PositiveSmallIntegerField()
    starting_from_price = models.PositiveIntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.from_place + ' to ' + self.to_place

    class Meta:
        verbose_name_plural = 'Popular Destinations'

class ride_types(models.Model):
    name = models.CharField(max_length=256)
    comment = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Ride Types'

class expected_time_hault(models.Model):
    ride_type = models.ForeignKey(ride_types, on_delete=models.DO_NOTHING)
    ride_time = models.IntegerField(verbose_name='Ride Time in Hours')
    hault_time = models.IntegerField(verbose_name='Hault time to be added in Minutes')

    def __str__(self):
        return self.ride_time

    class Meta:
        verbose_name_plural = 'Hault Time in Expected Journey Timme'

class city(models.Model):
    ride_types = models.ManyToManyField(ride_types)
    name = models.CharField(max_length=100, verbose_name='City Name')
    state = models.CharField(max_length=100)
    pickup = models.BooleanField(default=True)
    drop = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'

class location(models.Model):
    name = models.CharField(max_length=200)
    placeid = models.CharField(max_length=100)
    city = models.ForeignKey(city, on_delete=models.DO_NOTHING)
    pickup = models.BooleanField(default=0)
    drop = models.BooleanField(default=0)

    def __str__(self):
        return self.name

    def get_location(self):
        return str(self.name) + ', ' + str(self.city.name) + ', ' + str(self.city.state)

    class Meta:
        verbose_name_plural = 'Locations'

class airport(models.Model):
    name = models.CharField(max_length=200)
    placeid = models.CharField(max_length=100)
    city = models.ForeignKey(city, on_delete=models.DO_NOTHING)
    pickup = models.BooleanField(default=0)
    drop = models.BooleanField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Airports'

class ride_choices(models.Model):
    ride_type = models.ManyToManyField(ride_types)
    name = models.CharField(max_length=512)
    value = models.IntegerField()

    def __str__(self):
        return self.name

comfort_level_choices = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)
class car_types(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Car Types'

class car_attr(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Car Attributes'

class car_attr_comparison(models.Model):
    attr_name = models.ForeignKey(car_attr, on_delete=models.CASCADE)
    car_type = models.ForeignKey(car_types, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.attr_name.name

    class Meta:
        verbose_name_plural = 'Car Attribute Comparison Values'

class calc_attr(models.Model):
    name = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    value = models.FloatField(null=True, blank=True)
    is_multiplied = models.BooleanField(default=True)
    is_time_dependent = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Calculator Required Fields'


class calc_city_attr_value(models.Model):
    city1 = models.ForeignKey(city, related_name='city1', on_delete=models.DO_NOTHING, verbose_name='Pickup City')
    city2 = models.ForeignKey(city, related_name='city2', on_delete=models.DO_NOTHING, verbose_name='Drop City')
    car_type = models.ForeignKey(car_types, on_delete=models.DO_NOTHING)
    attr = models.ForeignKey(calc_attr, on_delete=models.DO_NOTHING)
    value = models.FloatField()

    class Meta:
        verbose_name_plural = 'Fares/Taxes between 2 cities'

class testimonials(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class faq(models.Model):
    title = models.CharField(max_length=100)
    answer = models.TextField()

    def str(self):
        return self.title

    class Meta:
        verbose_name_plural = 'FAQs'

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = 'Contact Us'


ride_status_choices = (
    ('Booked', 'Booked'),
    ('Ongoing', 'Ongoing'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
)
class ride_booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    phone_no = models.CharField(max_length=10)

    ride_type = models.ForeignKey('core.ride_types', on_delete=models.PROTECT)
    car_type = models.ForeignKey('core.car_types', on_delete=models.PROTECT)
    pickup = models.CharField(max_length=512)
    drop = models.CharField(max_length=512)
    distance = models.FloatField()
    duration = models.FloatField()

    additional_choices = models.ManyToManyField('core.ride_choices')
    additional_hault = models.PositiveSmallIntegerField(default=0)
    additional_pickup = models.CharField(max_length=256, blank=True, null=True)
    addtional_drop = models.CharField(max_length=256, blank=True, null=True)

    booking_datetime = models.DateTimeField(auto_now_add=True)
    pickup_datetime = models.DateTimeField()
    drop_datetime = models.DateTimeField()
    exact_pickup = models.CharField(max_length=512)
    exact_drop = models.CharField(max_length=512)

    initial_charges = models.IntegerField()
    additional_charges = models.PositiveSmallIntegerField()
    early_pickup_charges = models.PositiveSmallIntegerField()
    late_drop_charges = models.PositiveSmallIntegerField()
    night_charges = models.PositiveSmallIntegerField()
    gst_charges = models.PositiveSmallIntegerField()
    final_fare = models.PositiveSmallIntegerField()

    coupon = models.ForeignKey('customer.customer_promotional', on_delete=models.PROTECT, null=True, blank=True)
    balance_used = models.PositiveSmallIntegerField(default=0)

    final_ride_fare = models.PositiveSmallIntegerField()
    advance = models.PositiveSmallIntegerField()

    ride_status = models.CharField(max_length=10, choices=ride_status_choices)
    extra_remarks = models.TextField(blank=True, null=True)
    advance_payment_received = models.BooleanField(default=False)
    advance_15 = models.BooleanField(default=True)
    assigned_vendors = models.BooleanField(default=False)
    assigned_final_vendor = models.BooleanField(default=False)

    def get_advance(self):
        return float(self.final_ride_fare * 0.15)

    def amount_due(self):
        return float(self.final_ride_fare - self.advance)

    def __str__(self):
        return str(self.user) + str(self.id)

    class Meta:
        verbose_name_plural = 'User Bookings'

class payment(models.Model):
    booking = models.ForeignKey(ride_booking, on_delete=models.DO_NOTHING)
    txn_id = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    mode = models.CharField(max_length=56)

class assign_vendor(models.Model):
    booking = models.OneToOneField(ride_booking,on_delete=models.DO_NOTHING)
    commission = models.FloatField()
    vendors = models.ManyToManyField('vendor.vendorprofile')
    datetime = models.DateTimeField()

class vendorbids(models.Model):
    booking = models.ForeignKey(ride_booking, on_delete=models.DO_NOTHING)
    vendor = models.ForeignKey('vendor.vendorprofile', on_delete=models.CASCADE)
    max_bid = models.PositiveSmallIntegerField()
    bid = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

class final_ride_detail(models.Model):
    booking = models.OneToOneField('core.ride_booking', on_delete=models.DO_NOTHING)
    bid = models.ForeignKey('core.vendorbids', on_delete=models.DO_NOTHING)
    car = models.ForeignKey('vendor.vendor_cars', on_delete=models.DO_NOTHING, blank=True, null=True)
    driver = models.ForeignKey('vendor.driver', on_delete=models.DO_NOTHING, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
