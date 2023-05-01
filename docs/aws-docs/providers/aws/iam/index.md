---
title: iam
hide_title: false
hide_table_of_contents: false
keywords:
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
iam  
    
:::info Service Summary

<div class="row">
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>62</b></span><br />
<span>total selectable resources:&nbsp;<b>44</b></span><br />
<span>total methods:&nbsp;<b>156</b></span><br />
</div>
</div>

:::

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aws.iam</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>IAM</td></tr>
<tr><td><b>Description</b></td><td>iam</td></tr>
<tr><td><b>Id</b></td><td><code>iam:v23.04.00136</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/aws/iam/access_key_last_useds/">access_key_last_useds</a><br />
<a href="/providers/aws/iam/access_keys/">access_keys</a><br />
<a href="/providers/aws/iam/account_alias/">account_alias</a><br />
<a href="/providers/aws/iam/account_aliases/">account_aliases</a><br />
<a href="/providers/aws/iam/account_authorization_details/">account_authorization_details</a><br />
<a href="/providers/aws/iam/account_password_policies/">account_password_policies</a><br />
<a href="/providers/aws/iam/account_summaries/">account_summaries</a><br />
<a href="/providers/aws/iam/assume_role_policies/">assume_role_policies</a><br />
<a href="/providers/aws/iam/attached_group_policies/">attached_group_policies</a><br />
<a href="/providers/aws/iam/attached_role_policies/">attached_role_policies</a><br />
<a href="/providers/aws/iam/attached_user_policies/">attached_user_policies</a><br />
<a href="/providers/aws/iam/client_id_from_open_id_connect_providers/">client_id_from_open_id_connect_providers</a><br />
<a href="/providers/aws/iam/context_keys_for_custom_policies/">context_keys_for_custom_policies</a><br />
<a href="/providers/aws/iam/context_keys_for_principal_policies/">context_keys_for_principal_policies</a><br />
<a href="/providers/aws/iam/credential_reports/">credential_reports</a><br />
<a href="/providers/aws/iam/custom_policies/">custom_policies</a><br />
<a href="/providers/aws/iam/default_policy_versions/">default_policy_versions</a><br />
<a href="/providers/aws/iam/entities_for_policies/">entities_for_policies</a><br />
<a href="/providers/aws/iam/group_policies/">group_policies</a><br />
<a href="/providers/aws/iam/groups/">groups</a><br />
<a href="/providers/aws/iam/groups_for_users/">groups_for_users</a><br />
<a href="/providers/aws/iam/instance_profile_tags/">instance_profile_tags</a><br />
<a href="/providers/aws/iam/instance_profiles/">instance_profiles</a><br />
<a href="/providers/aws/iam/instance_profiles_for_roles/">instance_profiles_for_roles</a><br />
<a href="/providers/aws/iam/login_profiles/">login_profiles</a><br />
<a href="/providers/aws/iam/mfa_device_tags/">mfa_device_tags</a><br />
<a href="/providers/aws/iam/mfa_devices/">mfa_devices</a><br />
<a href="/providers/aws/iam/open_id_connect_provider_tags/">open_id_connect_provider_tags</a><br />
<a href="/providers/aws/iam/open_id_connect_provider_thumbprints/">open_id_connect_provider_thumbprints</a><br />
<a href="/providers/aws/iam/open_id_connect_providers/">open_id_connect_providers</a><br />
<a href="/providers/aws/iam/organizations_access_reports/">organizations_access_reports</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/aws/iam/passwords/">passwords</a><br />
<a href="/providers/aws/iam/policies/">policies</a><br />
<a href="/providers/aws/iam/policy_tags/">policy_tags</a><br />
<a href="/providers/aws/iam/policy_versions/">policy_versions</a><br />
<a href="/providers/aws/iam/principal_policies/">principal_policies</a><br />
<a href="/providers/aws/iam/role_descriptions/">role_descriptions</a><br />
<a href="/providers/aws/iam/role_from_instance_profiles/">role_from_instance_profiles</a><br />
<a href="/providers/aws/iam/role_permissions_boundaries/">role_permissions_boundaries</a><br />
<a href="/providers/aws/iam/role_policies/">role_policies</a><br />
<a href="/providers/aws/iam/role_tags/">role_tags</a><br />
<a href="/providers/aws/iam/role_to_instance_profiles/">role_to_instance_profiles</a><br />
<a href="/providers/aws/iam/roles/">roles</a><br />
<a href="/providers/aws/iam/saml_provider_tags/">saml_provider_tags</a><br />
<a href="/providers/aws/iam/saml_providers/">saml_providers</a><br />
<a href="/providers/aws/iam/security_token_service_preferences/">security_token_service_preferences</a><br />
<a href="/providers/aws/iam/server_certificate_tags/">server_certificate_tags</a><br />
<a href="/providers/aws/iam/server_certificates/">server_certificates</a><br />
<a href="/providers/aws/iam/service_last_accessed_details/">service_last_accessed_details</a><br />
<a href="/providers/aws/iam/service_last_accessed_details_with_entities/">service_last_accessed_details_with_entities</a><br />
<a href="/providers/aws/iam/service_linked_role_deletion_status/">service_linked_role_deletion_status</a><br />
<a href="/providers/aws/iam/service_linked_roles/">service_linked_roles</a><br />
<a href="/providers/aws/iam/service_specific_credentials/">service_specific_credentials</a><br />
<a href="/providers/aws/iam/signing_certificates/">signing_certificates</a><br />
<a href="/providers/aws/iam/ssh_public_keys/">ssh_public_keys</a><br />
<a href="/providers/aws/iam/user_from_groups/">user_from_groups</a><br />
<a href="/providers/aws/iam/user_permissions_boundaries/">user_permissions_boundaries</a><br />
<a href="/providers/aws/iam/user_policies/">user_policies</a><br />
<a href="/providers/aws/iam/user_tags/">user_tags</a><br />
<a href="/providers/aws/iam/user_to_groups/">user_to_groups</a><br />
<a href="/providers/aws/iam/users/">users</a><br />
<a href="/providers/aws/iam/virtual_mfa_devices/">virtual_mfa_devices</a><br />
</div>
</div>
