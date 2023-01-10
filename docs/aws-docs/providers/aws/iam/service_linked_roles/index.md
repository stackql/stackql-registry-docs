---
title: service_linked_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - service_linked_roles
  - iam
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_linked_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.service_linked_roles</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `service_linked_roles_Create` | `INSERT` | `AWSServiceName` | &lt;p&gt;Creates an IAM role that is linked to a specific Amazon Web Services service. The service controls the attached policies and when the role can be deleted. This helps ensure that the service is not broken by an unexpectedly changed or deleted role, which could put your Amazon Web Services resources into an unknown state. Allowing the service to control the role helps improve service stability and proper cleanup when a service and its role are no longer needed. For more information, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html"&gt;Using service-linked roles&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;To attach a policy to this service-linked role, you must make the request using the Amazon Web Services service that depends on this role.&lt;/p&gt; |
| `service_linked_roles_Delete` | `DELETE` | `RoleName` | &lt;p&gt;Submits a service-linked role deletion request and returns a &lt;code&gt;DeletionTaskId&lt;/code&gt;, which you can use to check the status of the deletion. Before you call this operation, confirm that the role has no active sessions and that any resources used by the role in the linked service are deleted. If you call this operation more than once for the same service-linked role and an earlier deletion task is not complete, then the &lt;code&gt;DeletionTaskId&lt;/code&gt; of the earlier request is returned.&lt;/p&gt; &lt;p&gt;If you submit a deletion request for a service-linked role whose linked service is still accessing a resource, then the deletion task fails. If it fails, the &lt;a&gt;GetServiceLinkedRoleDeletionStatus&lt;/a&gt; operation returns the reason for the failure, usually including the resources that must be deleted. To delete the service-linked role, you must first remove those resources from the linked service and then submit the deletion request again. Resources are specific to the service that is linked to the role. For more information about removing resources from a service, see the &lt;a href="http://docs.aws.amazon.com/"&gt;Amazon Web Services documentation&lt;/a&gt; for your service.&lt;/p&gt; &lt;p&gt;For more information about service-linked roles, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role"&gt;Roles terms and concepts: Amazon Web Services service-linked role&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
