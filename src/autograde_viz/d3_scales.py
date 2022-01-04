from selenium import webdriver

def d3_scale_linear(webdriver=webdriver.Chrome, \
                datum:float = None, \
                range_min:float = 0.0, \
                range_max:float = None, \
                domain_min:float = 0.0, \
                domain_max:float = None, \
                invert:bool = False)->float:
    """
    Constructs a d3 linear scale and returns position.
    Uses the Selenium webdriver (Chrome) to make a .js call
    Set invert=True to invert the range for the scale (e.g., vertical / y-scales)
    d3 must be loaded in the page being rendered
    """
    range_lower_bound = range_min
    range_upper_bound = range_max
    if invert:
        range_lower_bound = range_max
        range_upper_bound = range_min
    linear_scale_call = f"scale = d3.scaleLinear() \
        .range([{range_lower_bound}, {range_upper_bound}]) \
        .domain([{domain_min},{domain_max}]); \
        return scale({datum});"
    result = webdriver.execute_script(linear_scale_call)
    return result

    
def d3_scale_time(webdriver:webdriver.Chrome=None, \
                datum:str = None, \
                range_min:float = 0.0, \
                range_max:float = None, \
                domain_min:str = None, \
                domain_max:str = None, \
                invert:bool = False) -> float:
    """
    Constructs a d3 scaleTime (intended horizontal / x) and returns position
    Uses the Selenium webdriver to make a .js call
    d3 must be loaded in the page being rendered
    """
    range_lower_bound = range_min
    range_upper_bound = range_max
    if invert:
        range_lower_bound = range_max
        range_upper_bound = range_min

    scale_call = f"scale = d3.scaleTime().range([{range_min}, {range_max}])\
                .domain(d3.extent([d3.timeParse('%Y-%m-%e')('{domain_min}'),d3.timeParse('%Y-%m-%e')('{domain_max}')])); \
                return scale(d3.timeParse('%Y-%m-%e')('{datum}'));"
    result = webdriver.execute_script(scale_call)
    return result

def d3_scale_sqrt(webdriver=webdriver.Chrome, \
                datum:float = None, \
                range_min:float = 0.0, \
                range_max:float = None, \
                domain_min:float = 0.0, \
                domain_max:float = None, \
                invert:bool = False)->float:
    """
    Constructs a d3 square-root scale and returns position.
    Uses the Selenium webdriver (Chrome) to make a .js call
    Set invert=True to invert the range for the scale (e.g., vertical / y-scales)
    d3 must be loaded in the page being rendered
    """
    range_lower_bound = range_min
    range_upper_bound = range_max
    if invert:
        range_lower_bound = range_max
        range_upper_bound = range_min
    linear_scale_call = f"scale = d3.scaleSqrt() \
        .range([{range_lower_bound}, {range_upper_bound}]) \
        .domain([{domain_min},{domain_max}]); \
        return scale({datum});"
    result = webdriver.execute_script(linear_scale_call)
    return result

