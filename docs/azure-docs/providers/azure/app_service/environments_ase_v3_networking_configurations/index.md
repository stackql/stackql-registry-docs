---
title: environments_ase_v3_networking_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_ase_v3_networking_configurations
  - app_service
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

Creates, updates, deletes, gets or lists a <code>environments_ase_v3_networking_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_ase_v3_networking_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.environments_ase_v3_networking_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | AseV3NetworkingConfiguration resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get networking configuration of an App Service Environment |

## `SELECT` examples

Description for Get networking configuration of an App Service Environment


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.environments_ase_v3_networking_configurations
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```