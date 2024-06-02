---
title: org_policy_violations_previews
hide_title: false
hide_table_of_contents: false
keywords:
  - org_policy_violations_previews
  - policysimulator
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
<tr><td><b>Name</b></td><td><code>org_policy_violations_previews</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="policysimulator.org_policy_violations_previews" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the `OrgPolicyViolationsPreview`. It has the following format: `organizations/&#123;organization&#125;/locations/&#123;location&#125;/orgPolicyViolationsPreviews/&#123;orgPolicyViolationsPreview&#125;` Example: `organizations/my-example-org/locations/global/orgPolicyViolationsPreviews/506a5f7f` |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when this `OrgPolicyViolationsPreview` was created. |
| <CopyableCode code="customConstraints" /> | `array` | Output only. The names of the constraints against which all `OrgPolicyViolations` were evaluated. If `OrgPolicyOverlay` only contains `PolicyOverlay` then it contains the name of the configured custom constraint, applicable to the specified policies. Otherwise it contains the name of the constraint specified in `CustomConstraintOverlay`. Format: `organizations/&#123;organization_id&#125;/customConstraints/&#123;custom_constraint_id&#125;` Example: `organizations/123/customConstraints/custom.createOnlyE2TypeVms` |
| <CopyableCode code="overlay" /> | `object` | The proposed changes to OrgPolicy. |
| <CopyableCode code="resourceCounts" /> | `object` | A summary of the state of all resources scanned for compliance with the changed OrgPolicy. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the `OrgPolicyViolationsPreview`. |
| <CopyableCode code="violationsCount" /> | `integer` | Output only. The number of OrgPolicyViolations in this `OrgPolicyViolationsPreview`. This count may differ from `resource_summary.noncompliant_count` because each OrgPolicyViolation is specific to a resource **and** constraint. If there are multiple constraints being evaluated (i.e. multiple policies in the overlay), a single resource may violate multiple constraints. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_org_policy_violations_previews_get" /> | `SELECT` | <CopyableCode code="locationsId, orgPolicyViolationsPreviewsId, organizationsId" /> | GetOrgPolicyViolationsPreview gets the specified OrgPolicyViolationsPreview. Each OrgPolicyViolationsPreview is available for at least 7 days. |
| <CopyableCode code="organizations_locations_org_policy_violations_previews_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | ListOrgPolicyViolationsPreviews lists each OrgPolicyViolationsPreview in an organization. Each OrgPolicyViolationsPreview is available for at least 7 days. |
| <CopyableCode code="organizations_locations_org_policy_violations_previews_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | CreateOrgPolicyViolationsPreview creates an OrgPolicyViolationsPreview for the proposed changes in the provided OrgPolicyViolationsPreview.OrgPolicyOverlay. The changes to OrgPolicy are specified by this `OrgPolicyOverlay`. The resources to scan are inferred from these specified changes. |
| <CopyableCode code="_organizations_locations_org_policy_violations_previews_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | ListOrgPolicyViolationsPreviews lists each OrgPolicyViolationsPreview in an organization. Each OrgPolicyViolationsPreview is available for at least 7 days. |
