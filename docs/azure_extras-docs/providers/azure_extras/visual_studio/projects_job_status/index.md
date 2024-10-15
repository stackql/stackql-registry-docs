---
title: projects_job_status
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_job_status
  - visual_studio
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

Creates, updates, deletes, gets or lists a <code>projects_job_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects_job_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.visual_studio.projects_job_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Key/value pair of resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operation, resourceGroupName, resourceName, rootResourceName, subContainerName, subscriptionId" /> | Gets the status of the project resource creation job. |

## `SELECT` examples

Gets the status of the project resource creation job.


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_extras.visual_studio.projects_job_status
WHERE operation = '{{ operation }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND rootResourceName = '{{ rootResourceName }}'
AND subContainerName = '{{ subContainerName }}'
AND subscriptionId = '{{ subscriptionId }}';
```