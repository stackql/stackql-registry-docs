---
title: factories_data_plane_accesses
hide_title: false
hide_table_of_contents: false
keywords:
  - factories_data_plane_accesses
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>factories_data_plane_accesses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>factories_data_plane_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.factories_data_plane_accesses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessToken" /> | `string` | Data Plane read only access token. |
| <CopyableCode code="dataPlaneUrl" /> | `string` | Data Plane service base URL. |
| <CopyableCode code="policy" /> | `object` | Get Data Plane read only token request definition. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Get Data Plane access. |

## `SELECT` examples

Get Data Plane access.


```sql
SELECT
accessToken,
dataPlaneUrl,
policy
FROM azure.data_factory.factories_data_plane_accesses
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```