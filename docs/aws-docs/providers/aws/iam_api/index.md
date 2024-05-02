---
title: iam_api
hide_title: false
hide_table_of_contents: false
keywords:
  - iam_api
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
iam_api  
    
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
<tr><td><b>Name</b></td><td><code>aws.iam_api</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>iam_api</td></tr>
<tr><td><b>Description</b></td><td>iam_api</td></tr>
<tr><td><b>Id</b></td><td><code>iam_api:v00.00.00000</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/aws/iam_api/access_key_last_useds/">access_key_last_useds</a><br />
<a href="/providers/aws/iam_api/access_keys/">access_keys</a><br />
<a href="/providers/aws/iam_api/account_alias/">account_alias</a><br />
<a href="/providers/aws/iam_api/account_aliases/">account_aliases</a><br />
<a href="/providers/aws/iam_api/account_authorization_details/">account_authorization_details</a><br />
<a href="/providers/aws/iam_api/account_password_policies/">account_password_policies</a><br />
<a href="/providers/aws/iam_api/account_summaries/">account_summaries</a><br />
<a href="/providers/aws/iam_api/assume_role_policies/">assume_role_policies</a><br />
<a href="/providers/aws/iam_api/attached_group_policies/">attached_group_policies</a><br />
<a href="/providers/aws/iam_api/attached_role_policies/">attached_role_policies</a><br />
<a href="/providers/aws/iam_api/attached_user_policies/">attached_user_policies</a><br />
<a href="/providers/aws/iam_api/client_id_from_open_id_connect_providers/">client_id_from_open_id_connect_providers</a><br />
<a href="/providers/aws/iam_api/context_keys_for_custom_policies/">context_keys_for_custom_policies</a><br />
<a href="/providers/aws/iam_api/context_keys_for_principal_policies/">context_keys_for_principal_policies</a><br />
<a href="/providers/aws/iam_api/credential_reports/">credential_reports</a><br />
<a href="/providers/aws/iam_api/custom_policies/">custom_policies</a><br />
<a href="/providers/aws/iam_api/default_policy_versions/">default_policy_versions</a><br />
<a href="/providers/aws/iam_api/entities_for_policies/">entities_for_policies</a><br />
<a href="/providers/aws/iam_api/group_policies/">group_policies</a><br />
<a href="/providers/aws/iam_api/groups/">groups</a><br />
<a href="/providers/aws/iam_api/groups_for_users/">groups_for_users</a><br />
<a href="/providers/aws/iam_api/instance_profile_tags/">instance_profile_tags</a><br />
<a href="/providers/aws/iam_api/instance_profiles/">instance_profiles</a><br />
<a href="/providers/aws/iam_api/instance_profiles_for_roles/">instance_profiles_for_roles</a><br />
<a href="/providers/aws/iam_api/login_profiles/">login_profiles</a><br />
<a href="/providers/aws/iam_api/mfa_device_tags/">mfa_device_tags</a><br />
<a href="/providers/aws/iam_api/mfa_devices/">mfa_devices</a><br />
<a href="/providers/aws/iam_api/open_id_connect_provider_tags/">open_id_connect_provider_tags</a><br />
<a href="/providers/aws/iam_api/open_id_connect_provider_thumbprints/">open_id_connect_provider_thumbprints</a><br />
<a href="/providers/aws/iam_api/open_id_connect_providers/">open_id_connect_providers</a><br />
<a href="/providers/aws/iam_api/organizations_access_reports/">organizations_access_reports</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/aws/iam_api/passwords/">passwords</a><br />
<a href="/providers/aws/iam_api/policies/">policies</a><br />
<a href="/providers/aws/iam_api/policy_tags/">policy_tags</a><br />
<a href="/providers/aws/iam_api/policy_versions/">policy_versions</a><br />
<a href="/providers/aws/iam_api/principal_policies/">principal_policies</a><br />
<a href="/providers/aws/iam_api/role_descriptions/">role_descriptions</a><br />
<a href="/providers/aws/iam_api/role_from_instance_profiles/">role_from_instance_profiles</a><br />
<a href="/providers/aws/iam_api/role_permissions_boundaries/">role_permissions_boundaries</a><br />
<a href="/providers/aws/iam_api/role_policies/">role_policies</a><br />
<a href="/providers/aws/iam_api/role_tags/">role_tags</a><br />
<a href="/providers/aws/iam_api/role_to_instance_profiles/">role_to_instance_profiles</a><br />
<a href="/providers/aws/iam_api/roles/">roles</a><br />
<a href="/providers/aws/iam_api/saml_provider_tags/">saml_provider_tags</a><br />
<a href="/providers/aws/iam_api/saml_providers/">saml_providers</a><br />
<a href="/providers/aws/iam_api/security_token_service_preferences/">security_token_service_preferences</a><br />
<a href="/providers/aws/iam_api/server_certificate_tags/">server_certificate_tags</a><br />
<a href="/providers/aws/iam_api/server_certificates/">server_certificates</a><br />
<a href="/providers/aws/iam_api/service_last_accessed_details/">service_last_accessed_details</a><br />
<a href="/providers/aws/iam_api/service_last_accessed_details_with_entities/">service_last_accessed_details_with_entities</a><br />
<a href="/providers/aws/iam_api/service_linked_role_deletion_status/">service_linked_role_deletion_status</a><br />
<a href="/providers/aws/iam_api/service_linked_roles/">service_linked_roles</a><br />
<a href="/providers/aws/iam_api/service_specific_credentials/">service_specific_credentials</a><br />
<a href="/providers/aws/iam_api/signing_certificates/">signing_certificates</a><br />
<a href="/providers/aws/iam_api/ssh_public_keys/">ssh_public_keys</a><br />
<a href="/providers/aws/iam_api/user_from_groups/">user_from_groups</a><br />
<a href="/providers/aws/iam_api/user_permissions_boundaries/">user_permissions_boundaries</a><br />
<a href="/providers/aws/iam_api/user_policies/">user_policies</a><br />
<a href="/providers/aws/iam_api/user_tags/">user_tags</a><br />
<a href="/providers/aws/iam_api/user_to_groups/">user_to_groups</a><br />
<a href="/providers/aws/iam_api/users/">users</a><br />
<a href="/providers/aws/iam_api/virtual_mfa_devices/">virtual_mfa_devices</a><br />
</div>
</div>
