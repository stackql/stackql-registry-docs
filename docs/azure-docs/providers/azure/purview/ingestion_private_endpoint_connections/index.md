---
title: ingestion_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - ingestion_private_endpoint_connections
  - purview
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

Creates, updates, deletes, gets or lists a <code>ingestion_private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ingestion_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.ingestion_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the identifier. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="properties" /> | `object` | A private endpoint connection properties class. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all ingestion private endpoint connections |

## `SELECT` examples

Lists all ingestion private endpoint connections


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.purview.ingestion_private_endpoint_connections
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```