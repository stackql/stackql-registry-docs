---
title: provider_shared_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_shared_resources
  - stream_sharing
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_shared_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.stream_sharing.provider_shared_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | Description of shared resource |
| <CopyableCode code="_cloud_cluster" /> | `` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="cloud_cluster" /> | `object` | The cloud cluster to which this belongs. |
| <CopyableCode code="cluster_name" /> | `string` | The cluster display name of the shared resource. Deprecated |
| <CopyableCode code="crn" /> | `string` | Deprecated please use resources attribute. |
| <CopyableCode code="display_name" /> | `string` | Shared resource display name |
| <CopyableCode code="environment_name" /> | `string` | The environment name of the shared resource. Deprecated |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="logo_url" /> | `string` | Resource logo url |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="organization_contact" /> | `string` | Email of contact person from the organization |
| <CopyableCode code="organization_description" /> | `string` | Shared resource's organization description |
| <CopyableCode code="organization_name" /> | `` | Organization to which the shared resource belongs. Deprecated |
| <CopyableCode code="resources" /> | `array` | List of resource crns that are shared together |
| <CopyableCode code="schemas" /> | `array` | List of schemas in JSON format. This field is work in progress and subject to changes. |
| <CopyableCode code="tags" /> | `array` | list of tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cdx_v1provider_shared_resource" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read a provider shared resource. |
| <CopyableCode code="list_cdx_v1provider_shared_resources" /> | `SELECT` |  | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered, paginated list of all provider shared resources. |
| <CopyableCode code="delete_image_cdx_v1provider_shared_resource" /> | `DELETE` | <CopyableCode code="file_name, id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Deletes the image file for the shared resource |
| <CopyableCode code="update_cdx_v1provider_shared_resource" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to update a provider shared resource.<br /><br /> |
| <CopyableCode code="upload_image_cdx_v1provider_shared_resource" /> | `EXEC` | <CopyableCode code="file_name, id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Upload the image file for the shared resource |
| <CopyableCode code="view_image_cdx_v1provider_shared_resource" /> | `EXEC` | <CopyableCode code="file_name, id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Returns the image file for the shared resource |
