---
title: exports
hide_title: false
hide_table_of_contents: false
keywords:
  - exports
  - apigee
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.exports" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_analytics_exports_get" /> | `SELECT` | <CopyableCode code="environmentsId, exportsId, organizationsId" /> | Gets the details and status of an analytics export job. If the export job is still in progress, its `state` is set to "running". After the export job has completed successfully, its `state` is set to "completed". If the export job fails, its `state` is set to `failed`. |
| <CopyableCode code="organizations_environments_analytics_exports_list" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Lists the details and status of all analytics export jobs belonging to the parent organization and environment. |
| <CopyableCode code="organizations_environments_analytics_exports_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Submit a data export job to be processed in the background. If the request is successful, the API returns a 201 status, a URI that can be used to retrieve the status of the export job, and the `state` value of "enqueued". |
