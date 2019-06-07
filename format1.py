metro_areas = [
    ('Tokio', 'JP', 136.933, (1325.9898,132.0987)),
    ('Moskva', 'JP', 236.933, (2315.9898,132.0987)),
    ('Piter', 'JP', 336.933, (345.9898,-12.0987)),
    ('London', 'JP', 436.933, (435.9898,-13.0987)),
    ('Paris', 'JP', 536.933, (-55.9898,132.0987)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longtitude) in metro_areas:
        print(fmt.format(name, latitude, longtitude))

