---
title: answers
hide_title: false
hide_table_of_contents: false
keywords:
  - answers
  - mybusinessqanda
  - googlemybusiness    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googlemybusiness/stackql-googlemybusiness-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>answers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessqanda.answers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If the number of answers exceeds the requested max page size, this field is populated with a token to fetch the next page of answers on a subsequent call. If there are no more answers, this field is not present in the response. |
| `totalSize` | `integer` | The total number of answers posted for this question across all pages. |
| `answers` | `array` | The requested answers. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `locations_questions_answers_list` | `SELECT` | `locationsId, questionsId` | Returns the paginated list of answers for a specified question. |
| `locations_questions_answers_delete` | `DELETE` | `locationsId, questionsId` | Deletes the answer written by the current user to a question. |
| `locations_questions_answers_upsert` | `EXEC` | `locationsId, questionsId` | Creates an answer or updates the existing answer written by the user for the specified question. A user can only create one answer per question. |
