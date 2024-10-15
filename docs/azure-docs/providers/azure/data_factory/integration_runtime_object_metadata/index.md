---
title: integration_runtime_object_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_object_metadata
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

Creates, updates, deletes, gets or lists a <code>integration_runtime_object_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtime_object_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.integration_runtime_object_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Metadata id. |
| <CopyableCode code="name" /> | `string` | Metadata name. |
| <CopyableCode code="description" /> | `string` | Metadata description. |
| <CopyableCode code="type" /> | `string` | The type of SSIS object metadata. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Get a SSIS integration runtime object metadata by specified path. The return is pageable metadata list. |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Refresh a SSIS integration runtime object metadata. |

## `SELECT` examples

Get a SSIS integration runtime object metadata by specified path. The return is pageable metadata list.


```sql
SELECT
id,
name,
description,
type
FROM azure.data_factory.integration_runtime_object_metadata
WHERE factoryName = '{{ factoryName }}'
AND integrationRuntimeName = '{{ integrationRuntimeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```