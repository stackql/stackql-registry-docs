---
title: uptime_check_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - uptime_check_configs
  - monitoring
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>uptime_check_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.uptime_check_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A unique resource name for this Uptime check configuration. The format is: projects/[PROJECT_ID_OR_NUMBER]/uptimeCheckConfigs/[UPTIME_CHECK_ID] [PROJECT_ID_OR_NUMBER] is the Workspace host project associated with the Uptime check.This field should be omitted when creating the Uptime check configuration; on create, the resource name is assigned by the server and included in the response. |
| `selectedRegions` | `array` | The list of regions from which the check will be run. Some regions contain one location, and others contain more than one. If this field is specified, enough regions must be provided to include a minimum of 3 locations. Not specifying this field will result in Uptime checks running from all available regions. |
| `timeout` | `string` | The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Required. |
| `period` | `string` | How often, in seconds, the Uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5 minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 60s. |
| `resourceGroup` | `object` | The resource submessage for group checks. It can be used instead of a monitored resource, when multiple resources are being monitored. |
| `monitoredResource` | `object` | An object representing a resource that can be used for monitoring, logging, billing, or other purposes. Examples include virtual machine instances, databases, and storage devices such as disks. The type field identifies a MonitoredResourceDescriptor object that describes the resource's schema. Information in the labels field identifies the actual resource and its attributes according to the schema. For example, a particular Compute Engine VM instance could be represented by the following object, because the MonitoredResourceDescriptor for "gce_instance" has labels "project_id", "instance_id" and "zone": { "type": "gce_instance", "labels": { "project_id": "my-project", "instance_id": "12345678901234", "zone": "us-central1-a" }}  |
| `contentMatchers` | `array` | The content that is expected to appear in the data returned by the target server against which the check is run. Currently, only the first entry in the content_matchers list is supported, and additional entries will be ignored. This field is optional and should only be specified if a content match is required as part of the/ Uptime check. |
| `isInternal` | `boolean` | If this is true, then checks are made only from the 'internal_checkers'. If it is false, then checks are made only from the 'selected_regions'. It is an error to provide 'selected_regions' when is_internal is true, or to provide 'internal_checkers' when is_internal is false. |
| `checkerType` | `string` | The type of checkers to use to execute the Uptime check. |
| `displayName` | `string` | A human-friendly name for the Uptime check configuration. The display name should be unique within a Cloud Monitoring Workspace in order to make it easier to identify; however, uniqueness is not enforced. Required. |
| `internalCheckers` | `array` | The internal checkers that this check will egress from. If is_internal is true and this list is empty, the check will egress from all the InternalCheckers configured for the project that owns this UptimeCheckConfig. |
| `tcpCheck` | `object` | Information required for a TCP Uptime check request. |
| `httpCheck` | `object` | Information involved in an HTTP/HTTPS Uptime check request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_uptimeCheckConfigs_get` | `SELECT` | `projectsId, uptimeCheckConfigsId` | Gets a single Uptime check configuration. |
| `projects_uptimeCheckConfigs_list` | `SELECT` | `projectsId` | Lists the existing valid Uptime check configurations for the project (leaving out any invalid configurations). |
| `projects_uptimeCheckConfigs_create` | `INSERT` | `projectsId` | Creates a new Uptime check configuration. |
| `projects_uptimeCheckConfigs_delete` | `DELETE` | `projectsId, uptimeCheckConfigsId` | Deletes an Uptime check configuration. Note that this method will fail if the Uptime check configuration is referenced by an alert policy or other dependent configs that would be rendered invalid by the deletion. |
| `projects_uptimeCheckConfigs_patch` | `EXEC` | `projectsId, uptimeCheckConfigsId` | Updates an Uptime check configuration. You can either replace the entire configuration with a new one or replace only certain fields in the current configuration by specifying the fields to be updated via updateMask. Returns the updated configuration. |
