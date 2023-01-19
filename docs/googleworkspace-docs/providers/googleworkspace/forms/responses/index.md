---
title: responses
hide_title: false
hide_table_of_contents: false
keywords:
  - responses
  - forms
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.forms.responses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `createTime` | `string` | Output only. Timestamp for the first time the response was submitted. |
| `formId` | `string` | Output only. The form ID. |
| `lastSubmittedTime` | `string` | Output only. Timestamp for the most recent time the response was submitted. Does not track changes to grades. |
| `respondentEmail` | `string` | Output only. The email address (if collected) for the respondent. |
| `responseId` | `string` | Output only. The response ID. |
| `totalScore` | `number` | Output only. The total number of points the respondent received for their submission Only set if the form was a quiz and the response was graded. This includes points automatically awarded via autograding adjusted by any manual corrections entered by the form owner. |
| `answers` | `object` | Output only. The actual answers to the questions, keyed by question_id. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `forms_responses_get` | `SELECT` | `formId, responseId` | Get one response from the form. |
| `forms_responses_list` | `SELECT` | `formId` | List a form's responses. |
