---
title: region_autoscalers
hide_title: false
hide_table_of_contents: false
keywords:
  - region_autoscalers
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_autoscalers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_autoscalers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `autoscalingPolicy` | `object` | Cloud Autoscaler policy. |
| `statusDetails` | `array` | [Output Only] Human-readable details about the current state of the autoscaler. Read the documentation for Commonly returned status messages for examples of status messages you might encounter. |
| `recommendedSize` | `integer` | [Output Only] Target recommended MIG size (number of instances) computed by autoscaler. Autoscaler calculates the recommended MIG size even when the autoscaling policy mode is different from ON. This field is empty when autoscaler is not connected to an existing managed instance group or autoscaler did not generate its prediction. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `region` | `string` | [Output Only] URL of the region where the instance group resides (for autoscalers living in regional scope). |
| `status` | `string` | [Output Only] The status of the autoscaler configuration. Current set of possible values: - PENDING: Autoscaler backend hasn't read new/updated configuration. - DELETING: Configuration is being deleted. - ACTIVE: Configuration is acknowledged to be effective. Some warnings might be present in the statusDetails field. - ERROR: Configuration has errors. Actionable for users. Details are present in the statusDetails field. New values might be added in the future. |
| `target` | `string` | URL of the managed instance group that this autoscaler will scale. This field is required when creating an autoscaler. |
| `scalingScheduleStatus` | `object` | [Output Only] Status information of existing scaling schedules. |
| `zone` | `string` | [Output Only] URL of the zone where the instance group resides (for autoscalers living in zonal scope). |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#autoscaler for autoscalers. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `autoscaler, project, region` | Returns the specified autoscaler. |
| `list` | `SELECT` | `project, region` | Retrieves a list of autoscalers contained within the specified region. |
| `insert` | `INSERT` | `project, region` | Creates an autoscaler in the specified project using the data included in the request. |
| `delete` | `DELETE` | `autoscaler, project, region` | Deletes the specified autoscaler. |
| `patch` | `EXEC` | `project, region` | Updates an autoscaler in the specified project using the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| `update` | `EXEC` | `project, region` | Updates an autoscaler in the specified project using the data included in the request. |
