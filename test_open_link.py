import allure


@allure.id("26484")
@allure.title("Open link")
@allure.tag("web")
@allure.story("open links")
@allure.label("owner", "allure8")
@allure.feature("links")
def test_open_link():
    with allure.step("Open link link"):
        pass
    with allure.step("Check link"):
        with allure.step("Check url = link"):
            pass
