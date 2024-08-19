from Lesson7.Data_form.Pages.MainPage import MainPage
from Lesson7.Data_form.Pages.DataFildes import DataFild

def test_data_types(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.find_fields()
    main_page.fill_in_the_fields()
    main_page.submit_button()

    data_fild = DataFild(chrome_browser)
    data_fild.find_fields()
    data_fild.get_class_first_name()
    data_fild.get_class_last_name()
    data_fild.get_class_address()
    data_fild.get_class_email()
    data_fild.get_class_phone_number()
    data_fild.get_class_zip_code()
    data_fild.get_class_city()
    data_fild.get_class_country()
    data_fild.get_class_job_position()
    data_fild.get_class_company()

    assert "success" in data_fild.get_class_first_name()
    assert "success" in data_fild.get_class_last_name()
    assert "success" in data_fild.get_class_address()
    assert "success" in data_fild.get_class_email()
    assert "success" in data_fild.get_class_phone_number()
    assert "success" in data_fild.get_class_city()
    assert "success" in data_fild.get_class_country()
    assert "success" in data_fild.get_class_job_position()
    assert "success" in data_fild.get_class_company()
    assert "danger" in data_fild.get_class_zip_code()


