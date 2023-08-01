---
title: custom_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_modules
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>custom_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.custom_modules</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_security_health_analytics_settings_custom_modules_patch` | `EXEC` | `customModulesId, foldersId` | Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only. |
| `organizations_event_threat_detection_settings_custom_modules_get` | `EXEC` | `customModulesId, organizationsId` | Gets an Event Threat Detection custom module. |
| `organizations_event_threat_detection_settings_custom_modules_patch` | `EXEC` | `customModulesId, organizationsId` | Updates an Event Threat Detection custom module. |
| `organizations_security_health_analytics_settings_custom_modules_patch` | `EXEC` | `customModulesId, organizationsId` | Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only. |
| `projects_security_health_analytics_settings_custom_modules_patch` | `EXEC` | `customModulesId, projectsId` | Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only. |
