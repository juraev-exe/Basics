# Contributing to Basics

Thank you for your interest in contributing to our group project! This document provides guidelines and best practices for contributing to this repository.

## 🎯 Getting Started

1. **Fork the repository** (if you're not a direct collaborator) or **create a new branch**
2. **Set up your development environment** following the README.md instructions
3. **Choose an issue to work on** or create a new one to discuss your ideas

## 🌟 Contribution Workflow

### 1. Branch Naming Convention

Use descriptive branch names that indicate the type of work:

- `feature/add-user-authentication`
- `bugfix/fix-login-error`
- `docs/update-api-documentation`
- `refactor/improve-code-structure`

### 2. Making Changes

1. **Create a new branch** from `main`:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** in small, focused commits
3. **Test your changes** thoroughly
4. **Update documentation** if necessary

### 3. Commit Guidelines

Write clear, descriptive commit messages:

```bash
# Good examples:
git commit -m "Add user registration functionality"
git commit -m "Fix bug in password validation"
git commit -m "Update README with setup instructions"

# Avoid:
git commit -m "fix stuff"
git commit -m "updates"
```

### 4. Pull Request Process

1. **Push your branch** to the repository:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** with:
   - Clear title describing the changes
   - Detailed description of what was changed and why
   - Reference any related issues using `Fixes #123` or `Closes #123`
   - Screenshots for UI changes (if applicable)

3. **Request review** from team members
4. **Address feedback** and make necessary changes
5. **Squash commits** if requested before merging

## 📋 Code Standards

### Python Code Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Use type hints where appropriate

Example:
```python
def calculate_average(numbers: list[float]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average
        
    Returns:
        The average of the input numbers
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    return sum(numbers) / len(numbers)
```

### File Organization

- Keep related code together
- Use clear directory structure
- Add `__init__.py` files for Python packages
- Place tests in the `tests/` directory

## 🧪 Testing

- Write unit tests for new functions
- Ensure all tests pass before submitting PR
- Include both positive and negative test cases
- Use descriptive test names

Example test structure:
```python
def test_calculate_average_with_valid_numbers():
    """Test that calculate_average returns correct result with valid input."""
    result = calculate_average([1, 2, 3, 4, 5])
    assert result == 3.0

def test_calculate_average_with_empty_list():
    """Test that calculate_average raises ValueError with empty list."""
    with pytest.raises(ValueError):
        calculate_average([])
```

## 📚 Documentation

- Update README.md if you add new features
- Add inline comments for complex logic
- Document any new dependencies
- Include examples in docstrings

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Clear description** of the issue
2. **Steps to reproduce** the problem
3. **Expected behavior** vs actual behavior
4. **Environment details** (Python version, OS, etc.)
5. **Error messages** or screenshots if applicable

## 💡 Feature Requests

For new features, please:

1. **Check existing issues** to avoid duplicates
2. **Describe the feature** and its benefits
3. **Provide use cases** or examples
4. **Discuss implementation** approach if you have ideas

## 🤝 Code Review Guidelines

### For Authors:
- Keep PRs small and focused
- Provide context in PR description
- Respond to feedback promptly
- Test your changes thoroughly

### For Reviewers:
- Be constructive and respectful
- Focus on code quality and functionality
- Ask questions if something is unclear
- Approve when satisfied with changes

## 🚫 What Not to Do

- Don't commit directly to `main` branch
- Don't include sensitive information (passwords, API keys)
- Don't ignore linting errors or test failures
- Don't make unrelated changes in the same PR
- Don't forget to update documentation

## 📞 Getting Help

If you need help or have questions:

1. **Check existing issues** and documentation first
2. **Ask in GitHub Discussions** for general questions
3. **Create an issue** if you found a bug or have a specific question
4. **Tag team members** in your PR if you need specific review

## 🎉 Recognition

All contributors will be acknowledged in the project. We appreciate every contribution, from code to documentation to bug reports!

---

Thank you for contributing to our project! 🚀