---
title: databases_scans
hide_title: false
hide_table_of_contents: false
keywords:
  - databases_scans
  - spanner
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

Creates, updates, deletes or gets an <code>databases_scan</code> resource or lists <code>databases_scans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases_scans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.databases_scans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique name of the scan, specific to the Database service implementing this interface. |
| <CopyableCode code="details" /> | `object` | Additional information provided by the implementer. |
| <CopyableCode code="endTime" /> | `string` | The upper bound for when the scan is defined. |
| <CopyableCode code="scanData" /> | `object` | ScanData contains Cloud Key Visualizer scan data used by the caller to construct a visualization. |
| <CopyableCode code="startTime" /> | `string` | A range of time (inclusive) for when the scan is defined. The lower bound for when the scan is defined. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instances_databases_get_scans" /> | `SELECT` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Request a specific scan with Database-specific data for Cloud Key Visualizer. |

## `SELECT` examples

Request a specific scan with Database-specific data for Cloud Key Visualizer.

```sql
SELECT
name,
details,
endTime,
scanData,
startTime
FROM google.spanner.databases_scans
WHERE databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}'; 
```
