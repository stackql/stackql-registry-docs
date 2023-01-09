---
title: notification
hide_title: false
hide_table_of_contents: false
keywords:
  - notification
  - books
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.notification</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `doc_type` | `string` |  |
| `timeToExpireMs` | `string` |  |
| `doc_id` | `string` |  |
| `targetUrl` | `string` |  |
| `kind` | `string` | Resource type. |
| `iconUrl` | `string` |  |
| `title` | `string` |  |
| `crmExperimentIds` | `array` | The list of crm experiment ids. |
| `reason` | `string` |  |
| `notification_type` | `string` |  |
| `notificationGroup` | `string` |  |
| `pcampaign_id` | `string` |  |
| `show_notification_settings_action` | `boolean` |  |
| `body` | `string` |  |
| `is_document_mature` | `boolean` |  |
| `dont_show_notification` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `notification_id` |
