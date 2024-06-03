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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the API product subscription. |
| <CopyableCode code="apiproduct" /> | `string` | Name of the API product for which the developer is purchasing a subscription. |
| <CopyableCode code="createdAt" /> | `string` | Output only. Time when the API product subscription was created in milliseconds since epoch. |
| <CopyableCode code="endTime" /> | `string` | Time when the API product subscription ends in milliseconds since epoch. |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. Time when the API product subscription was last modified in milliseconds since epoch. |
| <CopyableCode code="startTime" /> | `string` | Time when the API product subscription starts in milliseconds since epoch. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_developers_subscriptions_get" /> | `SELECT` | <CopyableCode code="developersId, organizationsId, subscriptionsId" /> | Gets details for an API product subscription. |
| <CopyableCode code="organizations_developers_subscriptions_list" /> | `SELECT` | <CopyableCode code="developersId, organizationsId" /> | Lists all API product subscriptions for a developer. |
| <CopyableCode code="organizations_developers_subscriptions_create" /> | `INSERT` | <CopyableCode code="developersId, organizationsId" /> | Creates a subscription to an API product.  |
| <CopyableCode code="organizations_developers_subscriptions_expire" /> | `EXEC` | <CopyableCode code="developersId, organizationsId, subscriptionsId" /> | Expires an API product subscription immediately. |
