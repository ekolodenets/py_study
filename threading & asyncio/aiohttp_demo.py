import aiohttp
import asyncio


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.album_id = album_id
        self.photo_id = photo_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


def print_photo_title(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photos_by_album(task_name, album, session):
    print(f'{task_name=}')
    url = f'http://jsonplaceholder.typicode.com/photos?albumId={album}'

    response = await session.get(url)
    photo_json = await response.json()

    return [Photo.from_json(photo) for photo in photo_json]


async def main():
    # variant 1
    # async with aiohttp.ClientSession() as session:
    #     photos = await photos_by_album('Task 1', 3, session)
    #     print_photo_title(photos)
    # variant 1

    # variant 2
    async with aiohttp.ClientSession() as session:
        photos_in_albums = await asyncio.gather(*(photos_by_album(f'Task {i + 1}', album, session)
                                                  for i, album in enumerate(range(2, 30))))

        photos_count = sum([len(cur) for cur in photos_in_albums])
        print(f'{photos_count=}')
    # variant 2

if __name__ == '__main__':
    asyncio.run(main())
