---
title: scanned_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - scanned_resources
  - workloadmanager
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

Creates, updates, deletes or gets an <code>scanned_resource</code> resource or lists <code>scanned_resources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scanned_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workloadmanager.scanned_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resource" /> | `string` | resource name |
| <CopyableCode code="type" /> | `string` | resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="evaluationsId, executionsId, locationsId, projectsId" /> | List all scanned resources for a single Execution. |

## `SELECT` examples

List all scanned resources for a single Execution.

```sql
SELECT
resource,
type
FROM google.workloadmanager.scanned_resources
WHERE evaluationsId = '{{ evaluationsId }}'
AND executionsId = '{{ executionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
