---
title: integration_service_environment_managed_api_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environment_managed_api_operations
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_service_environment_managed_api_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_service_environment_managed_api_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_service_environment_managed_api_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The api operations properties |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apiName, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Gets the managed Api operations. |

## `SELECT` examples

Gets the managed Api operations.


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.logic_apps.integration_service_environment_managed_api_operations
WHERE apiName = '{{ apiName }}'
AND integrationServiceEnvironmentName = '{{ integrationServiceEnvironmentName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```