---
title: jobs_count
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_count
  - archive
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs_count</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.archive.jobs_count" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="failed" /> | `integer` | The total number of archive jobs with failed status for the archive source. |
| <CopyableCode code="ingesting" /> | `integer` | The total number of archive jobs with ingesting status for the archive source. |
| <CopyableCode code="pending" /> | `integer` | The total number of archive jobs with pending status for the archive source. |
| <CopyableCode code="scanning" /> | `integer` | The total number of archive jobs with scanning status for the archive source. |
| <CopyableCode code="sourceId" /> | `string` | Identifier for the archive source. |
| <CopyableCode code="succeeded" /> | `integer` | The total number of archive jobs with succeeded status for the archive source. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="listArchiveJobsCountPerSource" /> | `SELECT` | <CopyableCode code="region" /> |
