---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - clouderrorreporting
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouderrorreporting.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The group resource name. Written as `projects/&#123;projectID&#125;/groups/&#123;group_id&#125;`. Example: `projects/my-project-123/groups/my-group` In the group resource name, the `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). |
| <CopyableCode code="groupId" /> | `string` | An opaque identifier of the group. This field is assigned by the Error Reporting system and always populated. In the group resource name, the `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). |
| <CopyableCode code="resolutionStatus" /> | `string` | Error group's resolution status. An unspecified resolution status will be interpreted as OPEN |
| <CopyableCode code="trackingIssues" /> | `array` | Associated tracking issues. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupsId, projectsId" /> | Get the specified group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="groupsId, projectsId" /> | Replace the data for the specified group. Fails if the group does not exist. |
