import plotly.figure_factory as ff


def create_NY_FIPS():
    county_fips_range = range(1,124)
    county_fips_range = county_fips_range[::2]
    print(county_fips_range)
    fips_list = []

    for county in county_fips_range:
        print(county)
        fips = str(county)
        if len(fips) == 1:
            fips = '3600' + fips
        if len(fips) == 2:
            fips = '360' + fips
        if len(fips) == 3:
            fips = '36' + fips

        fips_list.append(fips)
    return fips_list

fips_list = create_NY_FIPS()

fig = ff.create_choropleth(fips=fips_list, scope=['New York'], values=range(1,124)[::2])
fig.layout.template = None
fig.show()
#print(fips_list)
