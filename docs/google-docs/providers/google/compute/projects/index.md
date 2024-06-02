---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="compute.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. This is *not* the project ID, and is just a unique ID used by Compute Engine to identify resources. |
| <CopyableCode code="name" /> | `string` | The project ID. For example: my-example-project. Use the project ID to make requests to Compute Engine. |
| <CopyableCode code="description" /> | `string` | An optional textual description of the resource. |
| <CopyableCode code="cloudArmorTier" /> | `string` | [Output Only] The Cloud Armor tier for this project. It can be one of the following values: CA_STANDARD, CA_ENTERPRISE_PAYGO. If this field is not specified, it is assumed to be CA_STANDARD. |
| <CopyableCode code="commonInstanceMetadata" /> | `object` | A metadata key/value entry. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="defaultNetworkTier" /> | `string` | This signifies the default network tier used for configuring resources of the project and can only take the following values: PREMIUM, STANDARD. Initially the default network tier is PREMIUM. |
| <CopyableCode code="defaultServiceAccount" /> | `string` | [Output Only] Default service account used by VMs running in this project. |
| <CopyableCode code="enabledFeatures" /> | `array` | Restricted features enabled for use on this project. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#project for projects. |
| <CopyableCode code="quotas" /> | `array` | [Output Only] Quotas assigned to this project. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="usageExportLocation" /> | `object` | The location in Cloud Storage and naming method of the daily usage report. Contains bucket_name and report_name prefix. |
| <CopyableCode code="vmDnsSetting" /> | `string` | [Output Only] Default internal DNS setting used by VMs running in this project. |
| <CopyableCode code="xpnProjectStatus" /> | `string` | [Output Only] The role this project has in a shared VPC configuration. Currently, only projects with the host role, which is specified by the value HOST, are differentiated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project" /> | Returns the specified Project resource. To decrease latency for this method, you can optionally omit any unneeded information from the response by using a field mask. This practice is especially recommended for unused quota information (the `quotas` field). To exclude one or more fields, set your request's `fields` query parameter to only include the fields you need. For example, to only include the `id` and `selfLink` fields, add the query parameter `?fields=id,selfLink` to your request. |
| <CopyableCode code="disable_xpn_host" /> | `EXEC` | <CopyableCode code="project" /> | Disable this project as a shared VPC host project. |
| <CopyableCode code="disable_xpn_resource" /> | `EXEC` | <CopyableCode code="project" /> | Disable a service resource (also known as service project) associated with this host project. |
| <CopyableCode code="enable_xpn_host" /> | `EXEC` | <CopyableCode code="project" /> | Enable this project as a shared VPC host project. |
| <CopyableCode code="enable_xpn_resource" /> | `EXEC` | <CopyableCode code="project" /> | Enable service resource (a.k.a service project) for a host project, so that subnets in the host project can be used by instances in the service project. |
| <CopyableCode code="move_disk" /> | `EXEC` | <CopyableCode code="project" /> | Moves a persistent disk from one zone to another. |
| <CopyableCode code="move_instance" /> | `EXEC` | <CopyableCode code="project" /> | Moves an instance and its attached persistent disks from one zone to another. *Note*: Moving VMs or disks by using this method might cause unexpected behavior. For more information, see the [known issue](/compute/docs/troubleshooting/known-issues#moving_vms_or_disks_using_the_moveinstance_api_or_the_causes_unexpected_behavior). [Deprecated] This method is deprecated. See [moving instance across zones](/compute/docs/instances/moving-instance-across-zones) instead. |
| <CopyableCode code="set_cloud_armor_tier" /> | `EXEC` | <CopyableCode code="project" /> | Sets the Cloud Armor tier of the project. To set ENTERPRISE or above the billing account of the project must be subscribed to Cloud Armor Enterprise. See Subscribing to Cloud Armor Enterprise for more information. |
| <CopyableCode code="set_common_instance_metadata" /> | `EXEC` | <CopyableCode code="project" /> | Sets metadata common to all instances within the specified project using the data included in the request. |
| <CopyableCode code="set_default_network_tier" /> | `EXEC` | <CopyableCode code="project" /> | Sets the default network tier of the project. The default network tier is used when an address/forwardingRule/instance is created without specifying the network tier field. |
| <CopyableCode code="set_usage_export_bucket" /> | `EXEC` | <CopyableCode code="project" /> | Enables the usage export feature and sets the usage export bucket where reports are stored. If you provide an empty request body using this method, the usage export feature will be disabled. |
