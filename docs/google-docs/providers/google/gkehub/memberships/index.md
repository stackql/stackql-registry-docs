---
title: memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - memberships
  - gkehub
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
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="gkehub.memberships" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full, unique name of this Membership resource in the format `projects/*/locations/*/memberships/&#123;membership_id&#125;`, set during creation. `membership_id` must be a valid RFC 1123 compliant DNS label: 1. At most 63 characters in length 2. It must consist of lower case alphanumeric characters or `-` 3. It must start and end with an alphanumeric character Which can be expressed as the regex: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`, with a maximum length of 63 characters. |
| <CopyableCode code="description" /> | `string` | Output only. Description of this membership, limited to 63 characters. Must match the regex: `a-zA-Z0-9*` This field is present for legacy purposes. |
| <CopyableCode code="authority" /> | `object` | Authority encodes how Google will recognize identities from this Membership. See the workload identity documentation for more details: https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity |
| <CopyableCode code="createTime" /> | `string` | Output only. When the Membership was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. When the Membership was deleted. |
| <CopyableCode code="endpoint" /> | `object` | MembershipEndpoint contains information needed to contact a Kubernetes API, endpoint and any additional Kubernetes metadata. |
| <CopyableCode code="externalId" /> | `string` | Optional. An externally-generated and managed ID for this Membership. This ID may be modified after creation, but this is not recommended. The ID must match the regex: `a-zA-Z0-9*` If this Membership represents a Kubernetes cluster, this value should be set to the UID of the `kube-system` namespace object. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels for this membership. |
| <CopyableCode code="lastConnectionTime" /> | `string` | Output only. For clusters using Connect, the timestamp of the most recent connection established with Google Cloud. This time is updated every several minutes, not continuously. For clusters that do not use GKE Connect, or that have never connected successfully, this field will be unset. |
| <CopyableCode code="monitoringConfig" /> | `object` | MonitoringConfig informs Fleet-based applications/services/UIs how the metrics for the underlying cluster is reported to cloud monitoring services. It can be set from empty to non-empty, but can't be mutated directly to prevent accidentally breaking the constinousty of metrics. |
| <CopyableCode code="state" /> | `object` | MembershipState describes the state of a Membership resource. |
| <CopyableCode code="uniqueId" /> | `string` | Output only. Google-generated UUID for this resource. This is unique across all Membership resources. If a Membership resource is deleted and another resource with the same name is created, it gets a different unique_id. |
| <CopyableCode code="updateTime" /> | `string` | Output only. When the Membership was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_memberships_get" /> | `SELECT` | <CopyableCode code="locationsId, membershipsId, projectsId" /> | Gets the details of a Membership. |
| <CopyableCode code="projects_locations_memberships_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Memberships in a given project and location. |
| <CopyableCode code="projects_locations_memberships_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Membership. **This is currently only supported for GKE clusters on Google Cloud**. To register other clusters, follow the instructions at https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster. |
| <CopyableCode code="projects_locations_memberships_delete" /> | `DELETE` | <CopyableCode code="locationsId, membershipsId, projectsId" /> | Removes a Membership. **This is currently only supported for GKE clusters on Google Cloud**. To unregister other clusters, follow the instructions at https://cloud.google.com/anthos/multicluster-management/connect/unregistering-a-cluster. |
| <CopyableCode code="_projects_locations_memberships_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Memberships in a given project and location. |
| <CopyableCode code="projects_locations_memberships_generate_connect_manifest" /> | `EXEC` | <CopyableCode code="locationsId, membershipsId, projectsId" /> | Generates the manifest for deployment of the GKE connect agent. **This method is used internally by Google-provided libraries.** Most clients should not need to call this method directly. |
| <CopyableCode code="projects_locations_memberships_patch" /> | `EXEC` | <CopyableCode code="locationsId, membershipsId, projectsId" /> | Updates an existing Membership. |
