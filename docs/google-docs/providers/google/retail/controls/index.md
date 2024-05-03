---
title: controls
hide_title: false
hide_table_of_contents: false
keywords:
  - controls
  - retail
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
<tr><td><b>Name</b></td><td><code>controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.controls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Fully qualified name `projects/*/locations/global/catalogs/*/controls/*` |
| <CopyableCode code="associatedServingConfigIds" /> | `array` | Output only. List of serving config ids that are associated with this control in the same Catalog. Note the association is managed via the ServingConfig, this is an output only denormalized view. |
| <CopyableCode code="displayName" /> | `string` | Required. The human readable control display name. Used in Retail UI. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is thrown. |
| <CopyableCode code="rule" /> | `object` | A rule is a condition-action pair * A condition defines when a rule is to be triggered. * An action specifies what occurs on that trigger. Currently rules only work for controls with SOLUTION_TYPE_SEARCH. |
| <CopyableCode code="searchSolutionUseCase" /> | `array` | Specifies the use case for the control. Affects what condition fields can be set. Only settable by search controls. Will default to SEARCH_SOLUTION_USE_CASE_SEARCH if not specified. Currently only allow one search_solution_use_case per control. |
| <CopyableCode code="solutionTypes" /> | `array` | Required. Immutable. The solution types that the control is used for. Currently we support setting only one type of solution at creation time. Only `SOLUTION_TYPE_SEARCH` value is supported at the moment. If no solution type is provided at creation time, will default to SOLUTION_TYPE_SEARCH. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_controls_get" /> | `SELECT` | <CopyableCode code="catalogsId, controlsId, locationsId, projectsId" /> | Gets a Control. |
| <CopyableCode code="projects_locations_catalogs_controls_list" /> | `SELECT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Lists all Controls by their parent Catalog. |
| <CopyableCode code="projects_locations_catalogs_controls_create" /> | `INSERT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Creates a Control. If the Control to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_catalogs_controls_delete" /> | `DELETE` | <CopyableCode code="catalogsId, controlsId, locationsId, projectsId" /> | Deletes a Control. If the Control to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="_projects_locations_catalogs_controls_list" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Lists all Controls by their parent Catalog. |
| <CopyableCode code="projects_locations_catalogs_controls_patch" /> | `EXEC` | <CopyableCode code="catalogsId, controlsId, locationsId, projectsId" /> | Updates a Control. Control cannot be set to a different oneof field, if so an INVALID_ARGUMENT is returned. If the Control to update does not exist, a NOT_FOUND error is returned. |
