---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - apigee
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
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the API product subscription. |
| `endTime` | `string` | Time when the API product subscription ends in milliseconds since epoch. |
| `lastModifiedAt` | `string` | Output only. Time when the API product subscription was last modified in milliseconds since epoch. |
| `startTime` | `string` | Time when the API product subscription starts in milliseconds since epoch. |
| `apiproduct` | `string` | Name of the API product for which the developer is purchasing a subscription. |
| `createdAt` | `string` | Output only. Time when the API product subscription was created in milliseconds since epoch. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_developers_subscriptions_get` | `SELECT` | `developersId, organizationsId, subscriptionsId` | Gets details for an API product subscription. |
| `organizations_developers_subscriptions_list` | `SELECT` | `developersId, organizationsId` | Lists all API product subscriptions for a developer. |
| `organizations_developers_subscriptions_create` | `INSERT` | `developersId, organizationsId` | Creates a subscription to an API product.  |
| `organizations_developers_subscriptions_expire` | `EXEC` | `developersId, organizationsId, subscriptionsId` | Expires an API product subscription immediately. |
