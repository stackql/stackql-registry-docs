---
title: books
hide_title: false
hide_table_of_contents: false
keywords:
  - books
  - libraryagent
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>books</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.libraryagent.books</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the book. Book names have the form `shelves/{shelf_id}/books/{book_id}`. The name is ignored when creating a book. |
| `author` | `string` | The name of the book author. |
| `read` | `boolean` | Value indicating whether the book has been read. |
| `title` | `string` | The title of the book. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `shelves_books_get` | `SELECT` | `booksId, shelvesId` | Gets a book. Returns NOT_FOUND if the book does not exist. |
| `shelves_books_list` | `SELECT` | `shelvesId` | Lists books in a shelf. The order is unspecified but deterministic. Newly created books will not necessarily be added to the end of this list. Returns NOT_FOUND if the shelf does not exist. |
| `shelves_books_borrow` | `EXEC` | `booksId, shelvesId` | Borrow a book from the library. Returns the book if it is borrowed successfully. Returns NOT_FOUND if the book does not exist in the library. Returns quota exceeded error if the amount of books borrowed exceeds allocation quota in any dimensions. |
| `shelves_books_return` | `EXEC` | `booksId, shelvesId` | Return a book to the library. Returns the book if it is returned to the library successfully. Returns error if the book does not belong to the library or the users didn't borrow before. |
