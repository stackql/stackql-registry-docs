---
title: xpn_host
hide_title: false
hide_table_of_contents: false
keywords:
  - xpn_host
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
<tr><td><b>Name</b></td><td><code>xpn_host</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.xpn_host</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. This is *not* the project ID, and is just a unique ID used by Compute Engine to identify resources. |
| `name` | `string` | The project ID. For example: my-example-project. Use the project ID to make requests to Compute Engine. |
| `description` | `string` | An optional textual description of the resource. |
| `enabledFeatures` | `array` | Restricted features enabled for use on this project. |
| `commonInstanceMetadata` | `object` | A metadata key/value entry. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#project for projects. |
| `vmDnsSetting` | `string` | [Output Only] Default internal DNS setting used by VMs running in this project. |
| `defaultServiceAccount` | `string` | [Output Only] Default service account used by VMs running in this project. |
| `defaultNetworkTier` | `string` | This signifies the default network tier used for configuring resources of the project and can only take the following values: PREMIUM, STANDARD. Initially the default network tier is PREMIUM. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `quotas` | `array` | [Output Only] Quotas assigned to this project. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `xpnProjectStatus` | `string` | [Output Only] The role this project has in a shared VPC configuration. Currently, only projects with the host role, which is specified by the value HOST, are differentiated. |
| `usageExportLocation` | `object` | The location in Cloud Storage and naming method of the daily usage report. Contains bucket_name and report_name prefix. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_xpn_host` | `SELECT` | `project` |
