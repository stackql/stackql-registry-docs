---
title: firewallpolicies
hide_title: false
hide_table_of_contents: false
keywords:
  - firewallpolicies
  - recaptchaenterprise
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
<tr><td><b>Name</b></td><td><code>firewallpolicies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recaptchaenterprise.firewallpolicies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results. It is set to empty if no policies remain in results. |
| `firewallPolicies` | `array` | Policy details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `firewallpoliciesId, projectsId` | Returns the specified firewall policy. |
| `list` | `SELECT` | `projectsId` | Returns the list of all firewall policies that belong to a project. |
| `create` | `INSERT` | `projectsId` | Creates a new FirewallPolicy, specifying conditions at which reCAPTCHA Enterprise actions can be executed. A project may have a maximum of 1000 policies. |
| `delete` | `DELETE` | `firewallpoliciesId, projectsId` | Deletes the specified firewall policy. |
| `patch` | `EXEC` | `firewallpoliciesId, projectsId` | Updates the specified firewall policy. |
