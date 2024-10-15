---
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
  - api_management
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

Creates, updates, deletes, gets or lists a <code>regions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.regions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Region name. |
| <CopyableCode code="isDeleted" /> | `boolean` | whether Region is deleted. |
| <CopyableCode code="isMasterRegion" /> | `boolean` | whether Region is the master region. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists all azure regions in which the service exists. |

## `SELECT` examples

Lists all azure regions in which the service exists.


```sql
SELECT
name,
isDeleted,
isMasterRegion
FROM azure.api_management.regions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```