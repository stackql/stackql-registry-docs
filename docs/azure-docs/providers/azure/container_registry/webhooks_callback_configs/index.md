---
title: webhooks_callback_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks_callback_configs
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>webhooks_callback_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhooks_callback_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.webhooks_callback_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="customHeaders" /> | `object` | Custom headers that will be added to the webhook notifications. |
| <CopyableCode code="serviceUri" /> | `string` | The service URI for the webhook to post notifications. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, webhookName" /> | Gets the configuration of service URI and custom headers for the webhook. |

## `SELECT` examples

Gets the configuration of service URI and custom headers for the webhook.


```sql
SELECT
customHeaders,
serviceUri
FROM azure.container_registry.webhooks_callback_configs
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webhookName = '{{ webhookName }}';
```