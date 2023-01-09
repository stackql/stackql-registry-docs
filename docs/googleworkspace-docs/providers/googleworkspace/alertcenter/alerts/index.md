---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - alertcenter
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.alertcenter.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `source` | `string` | Required. A unique identifier for the system that reported the alert. This is output only after alert is created. Supported sources are any of the following: * Google Operations * Mobile device management * Gmail phishing * Data Loss Prevention * Domain wide takeout * State sponsored attack * Google identity * Apps outage |
| `startTime` | `string` | Required. The time the event that caused this alert was started or detected. |
| `alertId` | `string` | Output only. The unique identifier for the alert. |
| `data` | `object` | Optional. The data associated with this alert, for example google.apps.alertcenter.type.DeviceCompromised. |
| `deleted` | `boolean` | Output only. `True` if this alert is marked for deletion. |
| `updateTime` | `string` | Output only. The time this alert was last updated. |
| `createTime` | `string` | Output only. The time this alert was created. |
| `metadata` | `object` | An alert metadata. |
| `type` | `string` | Required. The type of the alert. This is output only after alert is created. For a list of available alert types see [Google Workspace Alert types](https://developers.google.com/admin-sdk/alertcenter/reference/alert-types). |
| `etag` | `string` | Optional. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of an alert from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform alert updates in order to avoid race conditions: An `etag` is returned in the response which contains alerts, and systems are expected to put that etag in the request to update alert to ensure that their change will be applied to the same version of the alert. If no `etag` is provided in the call to update alert, then the existing alert is overwritten blindly. |
| `customerId` | `string` | Output only. The unique identifier of the Google account of the customer. |
| `endTime` | `string` | Optional. The time the event that caused this alert ceased being active. If provided, the end time must not be earlier than the start time. If not provided, it indicates an ongoing alert. |
| `securityInvestigationToolLink` | `string` | Output only. An optional [Security Investigation Tool](https://support.google.com/a/answer/7575955) query for this alert. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `alertId` | Gets the specified alert. Attempting to get a nonexistent alert returns `NOT_FOUND` error. |
| `list` | `SELECT` |  | Lists the alerts. |
| `delete` | `DELETE` | `alertId` | Marks the specified alert for deletion. An alert that has been marked for deletion is removed from Alert Center after 30 days. Marking an alert for deletion has no effect on an alert which has already been marked for deletion. Attempting to mark a nonexistent alert for deletion results in a `NOT_FOUND` error. |
| `batchDelete` | `EXEC` |  | Performs batch delete operation on alerts. |
| `batchUndelete` | `EXEC` |  | Performs batch undelete operation on alerts. |
| `undelete` | `EXEC` | `alertId` | Restores, or "undeletes", an alert that was marked for deletion within the past 30 days. Attempting to undelete an alert which was marked for deletion over 30 days ago (which has been removed from the Alert Center database) or a nonexistent alert returns a `NOT_FOUND` error. Attempting to undelete an alert which has not been marked for deletion has no effect. |
