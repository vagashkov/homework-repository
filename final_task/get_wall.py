import os

from sources.vk import VKSource

if __name__ == "__main__":

    # Define wall owner id
    owner_id = "12446354"
    cwd = os.getcwd()

    # Build new VKSource object for specified wall
    vk_source = VKSource(owner_id)

    # Create CSV-based description of the wall
    vk_source.process_wall_content(cwd + f"/{owner_id}" + ".csv")

    # Create JSON file to store posts statistics
    # vk_source.get_posts_statistics(cwd + f"/{owner_id}" + "_posts.txt")

    # Create JSON file to store details statistics
    # vk_source.get_posts_statistics(cwd + f"/{owner_id}" + "_details.txt")
