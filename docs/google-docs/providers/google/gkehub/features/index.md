---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
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
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkehub.features" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full, unique name of this Feature resource in the format `projects/*/locations/*/features/*`. |
| <CopyableCode code="createTime" /> | `string` | Output only. When the Feature resource was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. When the Feature resource was deleted. |
| <CopyableCode code="fleetDefaultMemberConfig" /> | `object` | CommonFleetDefaultMemberConfigSpec contains default configuration information for memberships of a fleet |
| <CopyableCode code="labels" /> | `object` | Labels for this Feature. |
| <CopyableCode code="membershipSpecs" /> | `object` | Optional. Membership-specific configuration for this Feature. If this Feature does not support any per-Membership configuration, this field may be unused. The keys indicate which Membership the configuration is for, in the form: `projects/&#123;p&#125;/locations/&#123;l&#125;/memberships/&#123;m&#125;` Where &#123;p&#125; is the project, &#123;l&#125; is a valid location and &#123;m&#125; is a valid Membership in this project at that location. &#123;p&#125; WILL match the Feature's project. &#123;p&#125; will always be returned as the project number, but the project ID is also accepted during input. If the same Membership is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. |
| <CopyableCode code="membershipStates" /> | `object` | Output only. Membership-specific Feature status. If this Feature does report any per-Membership status, this field may be unused. The keys indicate which Membership the state is for, in the form: `projects/&#123;p&#125;/locations/&#123;l&#125;/memberships/&#123;m&#125;` Where &#123;p&#125; is the project number, &#123;l&#125; is a valid location and &#123;m&#125; is a valid Membership in this project at that location. &#123;p&#125; MUST match the Feature's project number. |
| <CopyableCode code="resourceState" /> | `object` | FeatureResourceState describes the state of a Feature *resource* in the GkeHub API. See `FeatureState` for the "running state" of the Feature in the Hub and across Memberships. |
| <CopyableCode code="scopeSpecs" /> | `object` | Optional. Scope-specific configuration for this Feature. If this Feature does not support any per-Scope configuration, this field may be unused. The keys indicate which Scope the configuration is for, in the form: `projects/&#123;p&#125;/locations/global/scopes/&#123;s&#125;` Where &#123;p&#125; is the project, &#123;s&#125; is a valid Scope in this project. &#123;p&#125; WILL match the Feature's project. &#123;p&#125; will always be returned as the project number, but the project ID is also accepted during input. If the same Scope is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. |
| <CopyableCode code="scopeStates" /> | `object` | Output only. Scope-specific Feature status. If this Feature does report any per-Scope status, this field may be unused. The keys indicate which Scope the state is for, in the form: `projects/&#123;p&#125;/locations/global/scopes/&#123;s&#125;` Where &#123;p&#125; is the project, &#123;s&#125; is a valid Scope in this project. &#123;p&#125; WILL match the Feature's project. |
| <CopyableCode code="spec" /> | `object` | CommonFeatureSpec contains Hub-wide configuration information |
| <CopyableCode code="state" /> | `object` | CommonFeatureState contains Hub-wide Feature status information. |
| <CopyableCode code="updateTime" /> | `string` | Output only. When the Feature resource was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_features_get" /> | `SELECT` | <CopyableCode code="featuresId, locationsId, projectsId" /> | Gets details of a single Feature. |
| <CopyableCode code="projects_locations_features_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Features in a given project and location. |
| <CopyableCode code="projects_locations_features_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Adds a new Feature. |
| <CopyableCode code="projects_locations_features_delete" /> | `DELETE` | <CopyableCode code="featuresId, locationsId, projectsId" /> | Removes a Feature. |
| <CopyableCode code="projects_locations_features_patch" /> | `UPDATE` | <CopyableCode code="featuresId, locationsId, projectsId" /> | Updates an existing Feature. |
| <CopyableCode code="_projects_locations_features_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Features in a given project and location. |
