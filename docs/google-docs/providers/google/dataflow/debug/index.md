---
title: debug
hide_title: false
hide_table_of_contents: false
keywords:
  - debug
  - dataflow
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

Creates, updates, deletes, gets or lists a <code>debug</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>debug</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.debug" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_jobs_debug_send_capture" /> | `EXEC` | <CopyableCode code="jobId, projectId" /> | Send encoded debug capture data for component. |
| <CopyableCode code="projects_locations_jobs_debug_send_capture" /> | `EXEC` | <CopyableCode code="jobId, location, projectId" /> | Send encoded debug capture data for component. |
