---
title: pns_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - pns_credentials
  - notification_hubs
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>pns_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pns_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notification_hubs.pns_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Deprecated - only for compatibility. |
| <CopyableCode code="properties" /> | `object` | Collection of Notification Hub or Notification Hub Namespace PNS credentials. |
| <CopyableCode code="tags" /> | `object` | Deprecated - only for compatibility. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
location,
properties,
tags
FROM azure.notification_hubs.pns_credentials
WHERE namespaceName = '{{ namespaceName }}'
AND notificationHubName = '{{ notificationHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```