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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>xpn_host</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.xpn_host" /></td></tr>
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_xpn_host" /> | `SELECT` | <CopyableCode code="project" /> |
