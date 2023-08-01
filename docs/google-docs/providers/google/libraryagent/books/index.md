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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | The resource name of the book. Book names have the form `shelves/&#123;shelf_id&#125;/books/&#123;book_id&#125;`. The name is ignored when creating a book. |
| `title` | `string` | The title of the book. |
| `author` | `string` | The name of the book author. |
| `read` | `boolean` | Value indicating whether the book has been read. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `booksId, shelvesId` | Gets a book. Returns NOT_FOUND if the book does not exist. |
| `list` | `SELECT` | `shelvesId` | Lists books in a shelf. The order is unspecified but deterministic. Newly created books will not necessarily be added to the end of this list. Returns NOT_FOUND if the shelf does not exist. |
| `borrow` | `EXEC` | `booksId, shelvesId` | Borrow a book from the library. Returns the book if it is borrowed successfully. Returns NOT_FOUND if the book does not exist in the library. Returns quota exceeded error if the amount of books borrowed exceeds allocation quota in any dimensions. |
| `return` | `EXEC` | `booksId, shelvesId` | Return a book to the library. Returns the book if it is returned to the library successfully. Returns error if the book does not belong to the library or the users didn't borrow before. |
