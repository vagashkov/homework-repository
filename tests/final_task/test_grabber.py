import os
import sys


from final_task.sources.vk import VKSource


def test_wall_grabber():
    """Grab wall content into files and check it for existance."""
    # Define wall owner id
    owner_id = "12446354"
    cwd = os.getcwd()
    fields_list = VKSource.available_fields

    # Build new VKSource object for specified wall
    vk_source = VKSource(owner_id, fields_list=fields_list)

    # Define file name for CSV report
    csv_file = cwd + f"/final_task/{owner_id}" + ".csv"
    if os.path.exists(csv_file):
        os.remove(csv_file)

    # Create CSV-based description of the wall
    vk_source.process_wall_content(csv_file)
    assert os.path.exists(csv_file)

    # Create JSON file to store posts statistics
    posts_table = vk_source.get_posts_statistics_html()
    assert "table" in posts_table

    # Create JSON file to store details statistics
    details_table = vk_source.get_posts_statistics_html()
    assert "table" in details_table


def test_front_page():
    """Test for front page accessibility."""
    sys.path.insert(0, os.getcwd() + "/final_task")

    # Create Flask app object
    from final_task.app import create_app # noqa
    app = create_app()
    app.testing = True

    # Check if start page is accessible
    test_client = app.test_client()
    response = test_client.get("/index")
    assert response.status_code == 200
