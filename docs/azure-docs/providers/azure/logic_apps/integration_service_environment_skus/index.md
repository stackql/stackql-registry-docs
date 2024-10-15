---
title: integration_service_environment_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environment_skus
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

Creates, updates, deletes, gets or lists a <code>integration_service_environment_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_service_environment_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_service_environment_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | The integration service environment sku capacity. |
| <CopyableCode code="resourceType" /> | `string` | The resource type. |
| <CopyableCode code="sku" /> | `object` | The sku. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Gets a list of integration service environment Skus. |

## `SELECT` examples

Gets a list of integration service environment Skus.


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.logic_apps.integration_service_environment_skus
WHERE integrationServiceEnvironmentName = '{{ integrationServiceEnvironmentName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```