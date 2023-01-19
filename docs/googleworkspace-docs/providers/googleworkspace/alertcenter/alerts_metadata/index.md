---
title: alerts_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_metadata
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
<tr><td><b>Name</b></td><td><code>alerts_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.alertcenter.alerts_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Optional. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of an alert metadata from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform metadata updates in order to avoid race conditions: An `etag` is returned in the response which contains alert metadata, and systems are expected to put that etag in the request to update alert metadata to ensure that their change will be applied to the same version of the alert metadata. If no `etag` is provided in the call to update alert metadata, then the existing alert metadata is overwritten blindly. |
| `severity` | `string` | The severity value of the alert. Alert Center will set this field at alert creation time, default's to an empty string when it could not be determined. The supported values for update actions on this field are the following: * HIGH * MEDIUM * LOW |
| `status` | `string` | The current status of the alert. The supported values are the following: * NOT_STARTED * IN_PROGRESS * CLOSED |
| `updateTime` | `string` | Output only. The time this metadata was last updated. |
| `alertId` | `string` | Output only. The alert identifier. |
| `assignee` | `string` | The email address of the user assigned to the alert. |
| `customerId` | `string` | Output only. The unique identifier of the Google account of the customer. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `alerts_getMetadata` | `SELECT` | `alertId` |
