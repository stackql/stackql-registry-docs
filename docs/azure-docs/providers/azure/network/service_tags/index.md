---
title: service_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - service_tags
  - network
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

Creates, updates, deletes, gets or lists a <code>service_tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.service_tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the cloud. |
| <CopyableCode code="name" /> | `string` | The name of the cloud. |
| <CopyableCode code="changeNumber" /> | `string` | The iteration number. |
| <CopyableCode code="cloud" /> | `string` | The name of the cloud. |
| <CopyableCode code="nextLink" /> | `string` | The URL to get next page of service tag information resources. |
| <CopyableCode code="type" /> | `string` | The azure resource type. |
| <CopyableCode code="values" /> | `array` | The list of service tag information resources. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets a list of service tag information resources. |

## `SELECT` examples

Gets a list of service tag information resources.


```sql
SELECT
id,
name,
changeNumber,
cloud,
nextLink,
type,
values
FROM azure.network.service_tags
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```