---
title: questions
hide_title: false
hide_table_of_contents: false
keywords:
  - questions
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
<tr><td><b>Name</b></td><td><code>questions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessqanda.questions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If the number of questions exceeds the requested max page size, this field is populated with a token to fetch the next page of questions on a subsequent call. If there are no more questions, this field is not present in the response. |
| `questions` | `array` | The requested questions, |
| `totalSize` | `integer` | The total number of questions posted for this location across all pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `locations_questions_list` | `SELECT` | `locationsId` | Returns the paginated list of questions and some of its answers for a specified location. This operation is only valid if the specified location is verified. |
| `locations_questions_create` | `INSERT` | `locationsId` | Adds a question for the specified location. |
| `locations_questions_delete` | `DELETE` | `locationsId, questionsId` | Deletes a specific question written by the current user. |
| `locations_questions_patch` | `EXEC` | `locationsId, questionsId` | Updates a specific question written by the current user. |
