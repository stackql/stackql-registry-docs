---
title: service_perimeters
hide_title: false
hide_table_of_contents: false
keywords:
  - service_perimeters
  - accesscontextmanager
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
<tr><td><b>Name</b></td><td><code>service_perimeters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.accesscontextmanager.service_perimeters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name for the `ServicePerimeter`. Format: `accessPolicies/&#123;access_policy&#125;/servicePerimeters/&#123;service_perimeter&#125;`. The `service_perimeter` component must begin with a letter, followed by alphanumeric characters or `_`. After you create a `ServicePerimeter`, you cannot change its `name`. |
| `description` | `string` | Description of the `ServicePerimeter` and its use. Does not affect behavior. |
| `spec` | `object` | `ServicePerimeterConfig` specifies a set of Google Cloud resources that describe specific Service Perimeter configuration. |
| `status` | `object` | `ServicePerimeterConfig` specifies a set of Google Cloud resources that describe specific Service Perimeter configuration. |
| `title` | `string` | Human readable title. Must be unique within the Policy. |
| `useExplicitDryRunSpec` | `boolean` | Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. use_explicit_dry_run_spec must bet set to True if any of the fields in the spec are set to non-default values. |
| `perimeterType` | `string` | Perimeter type indicator. A single project or VPC network is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accessPoliciesId, servicePerimetersId` | Gets a service perimeter based on the resource name. |
| `list` | `SELECT` | `accessPoliciesId` | Lists all service perimeters for an access policy. |
| `create` | `INSERT` | `accessPoliciesId` | Creates a service perimeter. The long-running operation from this RPC has a successful status after the service perimeter propagates to long-lasting storage. If a service perimeter contains errors, an error response is returned for the first error encountered. |
| `delete` | `DELETE` | `accessPoliciesId, servicePerimetersId` | Deletes a service perimeter based on the resource name. The long-running operation from this RPC has a successful status after the service perimeter is removed from long-lasting storage. |
| `_list` | `EXEC` | `accessPoliciesId` | Lists all service perimeters for an access policy. |
| `commit` | `EXEC` | `accessPoliciesId` | Commits the dry-run specification for all the service perimeters in an access policy. A commit operation on a service perimeter involves copying its `spec` field to the `status` field of the service perimeter. Only service perimeters with `use_explicit_dry_run_spec` field set to true are affected by a commit operation. The long-running operation from this RPC has a successful status after the dry-run specifications for all the service perimeters have been committed. If a commit fails, it causes the long-running operation to return an error response and the entire commit operation is cancelled. When successful, the Operation.response field contains CommitServicePerimetersResponse. The `dry_run` and the `spec` fields are cleared after a successful commit operation. |
| `patch` | `EXEC` | `accessPoliciesId, servicePerimetersId` | Updates a service perimeter. The long-running operation from this RPC has a successful status after the service perimeter propagates to long-lasting storage. If a service perimeter contains errors, an error response is returned for the first error encountered. |
| `replace_all` | `EXEC` | `accessPoliciesId` | Replace all existing service perimeters in an access policy with the service perimeters provided. This is done atomically. The long-running operation from this RPC has a successful status after all replacements propagate to long-lasting storage. Replacements containing errors result in an error response for the first error encountered. Upon an error, replacement are cancelled and existing service perimeters are not affected. The Operation.response field contains ReplaceServicePerimetersResponse. |
