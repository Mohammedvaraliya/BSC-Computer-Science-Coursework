# flutter_image_gallery_pract_10

**Aim : Create an app using Flutter to implement an Image Gallery**

## Initializing a Flutter project.

1. Initialize a `Flutter` project using `flutter`.
    
    ```bash
    flutter create gallery_flutter_pract_10
    ```
    
2. Add Following Code in `main.dart` file
    
    ```dart
    import 'package:flutter/material.dart';
    import 'package:flutter_image_gallery_pract_10/gallery_page.dart';
    
    void main() {
      runApp(const MyApp());
    }
    
    class MyApp extends StatelessWidget {
      const MyApp({super.key});
    
      @override
      Widget build(BuildContext context) {
        return MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: ThemeData(
            primarySwatch: Colors.green,
            appBarTheme: const AppBarTheme(centerTitle: true),
          ),
          home: GalleryPage(),
        );
      }
    }
    ```
    
3. Create new dart file in `lib` directory named `gallery_page.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:cached_network_image/cached_network_image.dart';
    import 'package:flutter/material.dart';
    import 'package:flutter_image_gallery_pract_10/photo_view_page.dart';
    
    class GalleryPage extends StatelessWidget {
      GalleryPage({Key? key}) : super(key: key);
    
      final List<String> photos = [
        'https://images.unsplash.com/photo-1487017159836-4e23ece2e4cf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1471&q=80',
        'https://upload.wikimedia.org/wikipedia/commons/e/e7/Everest_North_Face_toward_Base_Camp_Tibet_Luca_Galuzzi_2006.jpg',
        'https://images.unsplash.com/photo-1490237014491-822aee911b99?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80',
        'https://images.unsplash.com/photo-1490598000245-075175152d25?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80',
        'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
        'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80',
        'https://images.unsplash.com/photo-1677430586198-c9e789c79561?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
        'https://images.unsplash.com/photo-1677253171066-b78ddca69a65?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80'
      ];
    
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: const Text("Gallery")),
          body: GridView.builder(
            physics: const BouncingScrollPhysics(
              parent: AlwaysScrollableScrollPhysics(),
            ),
            padding: const EdgeInsets.all(1),
            itemCount: photos.length,
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 3,
            ),
            itemBuilder: ((context, index) {
              return Container(
                padding: const EdgeInsets.all(0.5),
                child: InkWell(
                  onTap: () => Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (_) => PhotoViewPage(photos: photos, index: index),
                    ),
                  ),
                  child: Hero(
                    tag: photos[index],
                    child: CachedNetworkImage(
                      imageUrl: photos[index],
                      fit: BoxFit.cover,
                      placeholder: (context, url) => Container(color: Colors.grey),
                      errorWidget: (context, url, error) => Container(
                        color: Colors.red.shade400,
                      ),
                    ),
                  ),
                ),
              );
            }),
          ),
        );
      }
    }
    ```
    
4. Create new dart file in `lib` directory named `photo_view.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:cached_network_image/cached_network_image.dart';
    import 'package:flutter/material.dart';
    import 'package:photo_view/photo_view.dart';
    import 'package:photo_view/photo_view_gallery.dart';
    
    class PhotoViewPage extends StatelessWidget {
      final List<String> photos;
      final int index;
    
      const PhotoViewPage({
        Key? key,
        required this.photos,
        required this.index,
      }) : super(key: key);
    
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          extendBodyBehindAppBar: true,
          appBar: AppBar(
            backgroundColor: Colors.transparent,
            elevation: 0,
          ),
          body: PhotoViewGallery.builder(
            itemCount: photos.length,
            builder: (context, index) => PhotoViewGalleryPageOptions.customChild(
              child: CachedNetworkImage(
                imageUrl: photos[index],
                placeholder: (context, url) => Container(
                  color: Colors.grey,
                ),
                errorWidget: (context, url, error) => Container(
                  color: Colors.red.shade400,
                ),
              ),
              minScale: PhotoViewComputedScale.covered,
              heroAttributes: PhotoViewHeroAttributes(tag: photos[index]),
            ),
            pageController: PageController(initialPage: index),
            enableRotation: true,
          ),
        );
      }
    }
    ```
    

**Running a project**

**Connect Phone**

make sure USB debugging is enabled in Developer option

**Run The app**

```bash
flutter run main.dart
```

## Screenshots

![Frame 6](https://user-images.githubusercontent.com/95087498/221528188-1234006c-75a3-4e7c-94e8-4a6cb01f4f2f.png)


